let currentInput = '';
let operator = '';
let firstOperand = '';

function appendNumber(number) {
    currentInput += number;
    updateDisplay();
}

function setOperation(op) {
    if (currentInput === '') return;
    if (firstOperand !== '') {
        calculate();
    }
    operator = op;
    firstOperand = currentInput;
    currentInput = '';
}

async function calculate() {
    if (firstOperand === '' || currentInput === '') return;

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                a: firstOperand,
                b: currentInput,
                operation: operator
            })
        });

        const data = await response.json();

        if (response.ok) {
            currentInput = data.result.toString();
        } else {
            alert(data.error);
            currentInput = '';
        }

        operator = '';
        firstOperand = '';
        updateDisplay();
    } catch (error) {
        alert('An error occurred');
        currentInput = '';
        operator = '';
        firstOperand = '';
        updateDisplay();
    }
}

function clearDisplay() {
    currentInput = '';
    operator = '';
    firstOperand = '';
    updateDisplay();
}

function updateDisplay() {
    document.getElementById('display').innerText = currentInput || '0';
}
