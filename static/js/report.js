fetch("/api/student")
  .then(res => res.json())
  .then(data => {

    if (data.error) {
      alert(data.error);
      return;
    }
    let maths = Number(data.Maths);
    let ds = Number(data.DS);
    let os = Number(data.OS);
    let dbms = Number(data.DBMS);
    let ai = Number(data.AI);

    let avg = (maths + ds + os + dbms + ai) / 5;
    let result = "";

    if (avg >= 80) {
        result = "Excellent";
    } else if (avg >= 60) {
        result = "Good";
    } else if (avg >= 40) {
        result = "Average";
    } else {
        result = "Poor";
    }
    document.getElementById("roll").innerText = data.Roll_No;
    document.getElementById("name").innerText = data.Name;
    document.getElementById("branch").innerText = data.Branch;
    document.getElementById("FP").innerText = avg;
    document.getElementById("PP").innerText = result;
    
  
  });