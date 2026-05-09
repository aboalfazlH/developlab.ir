const password = document.getElementById("id_password1");
const password2 = document.getElementById("id_password2");
const email = document.getElementById("id_email");
const username = document.getElementById("id_username");
const firstName = document.getElementById("id_first_name");
const lastName = document.getElementById("id_last_name");
const passwordLengthError = document.getElementById("err-1");
const passwordNumericError = document.getElementById("err-2");
const passwordTrueError = document.getElementById("err-3");
const uniqueUsernameError = document.getElementById("err-4");
const uniqueEmailError = document.getElementById("err-5");
const fullNameError = document.getElementById("err-6");
const btn = document.getElementById('submit-btn');
const apiBaseUrl = `http://${window.location.host}/accounts/api/users/is_exist/`;

let isPasswordLengthValid = false;
let isPasswordNumericValid = false;
let firstNameNotBlank = false;
let lastNameNotBlank = false;
let arePasswordsMatching = false;
let isUsernameUnique = false;
let isEmailUnique = false;

function updateButtonState() {
    const allValid = isPasswordLengthValid &&
                     isPasswordNumericValid &&
                     arePasswordsMatching &&
                     firstNameNotBlank &&
                     lastNameNotBlank &&
                     isUsernameUnique &&
                     isEmailUnique;

    if (allValid) {
        btn.disabled = false;
    } else {
        btn.disabled = true;
    }
}

function validateForm() {
    const passwordValue = password.value;
    const passwordValue2 = password2.value;

    if (passwordValue.length < 8) {
        passwordLengthError.style.color = "red";
        isPasswordLengthValid = false;
    } else {
        passwordLengthError.style.color = "green";
        isPasswordLengthValid = true;
    }

    if (isNaN(passwordValue) == false) {
        passwordNumericError.style.color = "red";
        isPasswordNumericValid = false;
    } else {
        passwordNumericError.style.color = "green";
        isPasswordNumericValid = true;
    }

    if (passwordValue !== passwordValue2) {
        passwordTrueError.style.color = "red";
        arePasswordsMatching = false;
    } else {
        passwordTrueError.style.color = "green";
        arePasswordsMatching = true;
    }

    if (firstName.value && lastName.value) {
        fullNameError.style.color = "green";
        firstNameNotBlank = true;
        lastNameNotBlank = true;
    } else {
        fullNameError.style.color = "red";
        firstNameNotBlank = false;
        lastNameNotBlank = false;
    }

    updateButtonState();

    const eValue = email.value || null;
    const uValue = username.value || null;

    if (eValue || uValue) {
        fetch(`${apiBaseUrl}?email=${eValue}&username=${uValue}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.email_is_exists) {
                    uniqueEmailError.style.color = "red";
                    isEmailUnique = false;
                } else {
                    uniqueEmailError.style.color = "green";
                    isEmailUnique = true;
                }
                if (data.username_is_exists) {
                    uniqueUsernameError.style.color = "red";
                    isUsernameUnique = false;
                } else {
                    uniqueUsernameError.style.color = "green";
                    isUsernameUnique = true;
                }
            })
            .catch(error => {
                console.error('Error during fetch:', error);
                isUsernameUnique = false;
                isEmailUnique = false;
                uniqueUsernameError.style.color = "red";
                uniqueEmailError.style.color = "red";
            })
            .finally(() => {
                updateButtonState();
            });
    } else {
        uniqueEmailError.style.color = "green";
        isEmailUnique = true;
        uniqueUsernameError.style.color = "green";
        isUsernameUnique = true;
        updateButtonState();
    }
}

password.addEventListener("input", validateForm);
password.addEventListener("change", validateForm);
password2.addEventListener("input", validateForm);
password2.addEventListener("change", validateForm);
firstName.addEventListener("input", validateForm);
firstName.addEventListener("change", validateForm);
lastName.addEventListener("input", validateForm);
lastName.addEventListener("change", validateForm);
email.addEventListener("change", validateForm);
username.addEventListener("change", validateForm);

validateForm();
