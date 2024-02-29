// Get the result input element
const resultElement = document.getElementById('result');

// Function to insert characters into the result input element
function insert(character) {
  resultElement.value += character;
}

// Function to calculate the result of the expression in the result input element
function calculate() {
  try {
    resultElement.value = eval(resultElement.value);
  } catch (error) {
    resultElement.value = 'Error';
  }
}

// Function to clear the result input element
function clearResult() {
  resultElement.value = '';
}


// Function to calculate the square root of the value in the result input element
function squareRoot() {
  try {
    resultElement.value = Math.sqrt(resultElement.value);
  } catch (error) {
    resultElement.value = 'Error';
  }
}

// Function to calculate the power of the value in the result input element
function power() {
  try {
    resultElement.value = Math.pow(resultElement.value, 2);
  } catch (error) {
    resultElement.value = 'Error';
  }
}

// Function to calculate the sine of the value in the result input element
function sine() {
  try {
    resultElement.value = Math.sin(resultElement.value);
  } catch (error) {
    resultElement.value = 'Error';
  }
}

// Function to calculate the cosine of the value in the result input element
function cosine() {
  try {
    resultElement.value = Math.cos(resultElement.value);
  } catch (error) {
    resultElement.value = 'Error';
  }
}

// Function to calculate the tangent of the value in the result input element
function tangent() {
  try {
    resultElement.value = Math.tan(resultElement.value);
  } catch (error) {
    resultElement.value = 'Error';
  }
}

// Function to calculate the logarithm of the value in the result input element
function logarithm() {
  try {
    resultElement.value = Math.log(resultElement.value);
  } catch (error) {
    resultElement.value = 'Error';
  }
}

// Function to calculate the exponential of the value in the result input element
function exponential() {
  try {
    resultElement.value = Math.exp(resultElement.value);
  } catch (error) {
    resultElement.value = 'Error';
  }
}
