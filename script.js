document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Get form values
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const gender = document.getElementById("gender").value;
    const age = document.getElementById("age").value;
    const phone = document.getElementById("phone").value;
    const address = document.getElementById("address").value;
    const state = document.getElementById("state").value;
    const country = document.getElementById("country").value;
    const selectedLanguages = Array.from(document.getElementById("languages").selectedOptions).map(option => option.value);
  
    // Check if passwords match
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }
  
    // Create an object with the form data
    const formData = {
      firstName: firstName,
      lastName: lastName,
      email: email,
      password: password,
      gender: gender,
      age: age,
      phone: phone,
      address: address,
      state: state,
      country: country,
      languages: selectedLanguages
      // You can add more fields as needed
    };
  
    // Here, you can perform further actions like sending data to a server or processing it
    console.log(formData);
    alert("Registration successful!");
  });
  