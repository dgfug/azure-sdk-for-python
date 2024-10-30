# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import numbers
import json
from opentelemetry.sdk.trace import Span


class GenAiTraceVerifier:

    def check_span_attributes(self, span, attributes):
        # Convert the list of tuples to a dictionary for easier lookup
        attribute_dict = dict(attributes)

        for attribute_name in span.attributes.keys():
            # Check if the attribute name exists in the input attributes
            if attribute_name not in attribute_dict:
                return False

            attribute_value = attribute_dict[attribute_name]
            if isinstance(attribute_value, list):
                # Check if the attribute value in the span matches the provided list
                if span.attributes[attribute_name] != attribute_value:
                    return False
            elif isinstance(attribute_value, tuple):
                # Check if the attribute value in the span matches the provided list
                if span.attributes[attribute_name] != attribute_value:
                    return False
            else:
                # Check if the attribute value matches the provided value
                if attribute_value == "+":
                    if not isinstance(span.attributes[attribute_name], numbers.Number):
                        return False
                    if span.attributes[attribute_name] < 0:
                        return False
                elif attribute_value != "" and span.attributes[attribute_name] != attribute_value:
                    return False
                # Check if the attribute value in the span is not empty when the provided value is ""
                elif attribute_value == "" and not span.attributes[attribute_name]:
                    return False

        return True

    def is_valid_json(self, my_string):
        try:
            json_object = json.loads(my_string)
        except ValueError as e1:
            return False
        except TypeError as e2:
            return False
        return True

    def check_json_string(self, expected_json, actual_json):
        if self.is_valid_json(expected_json) and self.is_valid_json(actual_json):
            return self.check_event_attributes(json.loads(expected_json), json.loads(actual_json))
        else:
            return False

    def check_event_attributes(self, expected_dict, actual_dict):
        if set(expected_dict.keys()) != set(actual_dict.keys()):
            return False
        for key, expected_val in expected_dict.items():
            if key not in actual_dict:
                return False
            actual_val = actual_dict[key]

            if self.is_valid_json(expected_val):
                if not self.is_valid_json(actual_val):
                    return False
                if not self.check_json_string(expected_val, actual_val):
                    return False
            elif isinstance(expected_val, dict):
                if not isinstance(actual_val, dict):
                    return False
                if not self.check_event_attributes(expected_val, actual_val):
                    return False
            elif isinstance(expected_val, list):
                if not isinstance(actual_val, list):
                    return False
                if len(expected_val) != len(actual_val):
                    return False
                for expected_list, actual_list in zip(expected_val, actual_val):
                    if not self.check_event_attributes(expected_list, actual_list):
                        return False
            elif isinstance(expected_val, str) and expected_val == "*":
                if actual_val == "":
                    return False
            elif expected_val != actual_val:
                return False
        return True

    def check_span_events(self, span, expected_events):
        span_events = list(span.events)  # Create a list of events from the span

        for expected_event in expected_events:
            for actual_event in span_events:
                if expected_event["name"] == actual_event.name:
                    if not self.check_event_attributes(expected_event["attributes"], actual_event.attributes):
                        return False
                    span_events.remove(actual_event)  # Remove the matched event from the span_events
                    break
            else:
                return False  # If no match found for an expected event

        if len(span_events) > 0:  # If there are any additional events in the span_events
            return False

        return True
