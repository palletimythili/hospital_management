
const API = "http://127.0.0.1:5000/patients";

async function addPatient() {
    const patient = {
        name: document.getElementById("name").value,
        age: document.getElementById("age").value,
        gender: document.getElementById("gender").value,
        disease: document.getElementById("disease").value
    };

    if (!patient.name || !patient.age ||
        !patient.gender || !patient.disease) {
        alert("Please fill all fields");
        return;
    }

    const response = await fetch(API, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(patient)
    });

    if (response.ok) {
        alert("Patient Added Successfully");
        loadPatients();
    }
}

async function loadPatients() {
    const response = await fetch(API);
    const data = await response.json();

    document.getElementById("patients").innerHTML =
        data.map(p => `
            <div>
                ${p.name} | ${p.age} | ${p.gender} | ${p.disease}
                <button onclick="deletePatient(${p.id})">Delete</button>
            </div>
        `).join("");
}

async function deletePatient(id) {
    await fetch(`${API}/${id}`, {method: "DELETE"});
    loadPatients();
}

loadPatients();
