const form = document.querySelector("#insurance-form");
const resultCard = document.querySelector("#result-card");
const prediction = document.querySelector("#prediction");
const errorMessage = document.querySelector("#error-message");
console.log("JavaScript loaded");
console.log(form);
//  console.log() -->"Print this value to the browser's developer console so I can see/debug it."

form.addEventListener("submit", async function(event) {
    event.preventDefault();
    const formData = new FormData(form);
    const data = {
        age: Number(formData.get("age")),
        sex: formData.get("sex"),
        bmi: Number(formData.get("bmi")),
        children: Number(formData.get("children")),
        smoker: formData.get("smoker"),
        region: formData.get("region")
    };

errorMessage.style.display = "none";
    const response= await fetch("http://127.0.0.1:8000/predict", {
        method:"POST", 
        headers: {
            "Content-type": "application/json"
        },
        body:JSON.stringify(data)
    });


    const result = await response.json();

    if(!response.ok){
        console.log("API Error: ", result);
        prediction.textContent = "";
        errorMessage.textContent = "Please check your input values";
        errorMessage.style.display="block";
        resultCard.style.display="block";
        return;
    }


    prediction.textContent = `$${result.predicted_charge.toFixed(2)}`;
    resultCard.style.display = "block";
    
    // console.log(Object.fromEntries(formData));
    // Object.fromEntries() converts the FormData entries into a normal JavaScript object.
});