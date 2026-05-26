
// PERFORMANCE PREDICTION LOGIC


function predictPerformance() {

    let Att = Number(document.getElementById("attendance").value);
    let Sem = Number(document.getElementById("semester").value);
    let maths = Number(document.getElementById("maths").value);
    let ds = Number(document.getElementById("ds").value);
    let os = Number(document.getElementById("os").value);
    let dbms = Number(document.getElementById("dbms").value);
    let ai = Number(document.getElementById("ai").value);

    if (!Att || !Sem || !maths || !ds || !os || !dbms || !ai) {
        alert("Please enter all marks");
        return;
    }

    let avg = (maths + ds + os + dbms + ai) / 5;
    let result = "";
    Average = (avg+Sem)/2;

    if (Average >= 80 && Att>=80) {
        result = "Excellent";
    } else if (Average >= 70 && Att>=60) {
        result = "Good";
    } else if (Average >= 55 && Att>=40) {
        result = "Average";
    } else {
        result = "Poor";
    }

    

    document.getElementById("result").innerHTML =
        `Predicted Performance: <b style="color:green">${result}</b>
         <br> Expected Percentage: <b>${Average.toFixed(2)}%</b>`;
}