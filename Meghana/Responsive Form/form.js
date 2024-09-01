function validate(e){
    e.preventDefault();

    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgBox = document.getElementById("message").value;

    let message = '';

    if (email === ''){
        message = "Please enter a valid email.";
        msgBox.style.color = "red";
    }
    if (pass === ''){
        message = "Your password should have a minimum of 8 characters.";
        msgBox.style.color = "red";
    }
    if (age === ''){
        message = "Your age must be between 12 and 50.";
        msgBox.style.color = "red";
    }

    else{
        message = "Login Successful!"
        msgBox.style.color = "green";
    }

    msgBox.innerHTML = message;
}