
"use strict";

let IoTSensor = require('./IoTSensor.js');
let iot_sensor = require('./iot_sensor.js');
let FibonacciAction = require('./FibonacciAction.js');
let FibonacciFeedback = require('./FibonacciFeedback.js');
let FibonacciResult = require('./FibonacciResult.js');
let FibonacciActionGoal = require('./FibonacciActionGoal.js');
let FibonacciActionFeedback = require('./FibonacciActionFeedback.js');
let FibonacciActionResult = require('./FibonacciActionResult.js');
let FibonacciGoal = require('./FibonacciGoal.js');

module.exports = {
  IoTSensor: IoTSensor,
  iot_sensor: iot_sensor,
  FibonacciAction: FibonacciAction,
  FibonacciFeedback: FibonacciFeedback,
  FibonacciResult: FibonacciResult,
  FibonacciActionGoal: FibonacciActionGoal,
  FibonacciActionFeedback: FibonacciActionFeedback,
  FibonacciActionResult: FibonacciActionResult,
  FibonacciGoal: FibonacciGoal,
};
