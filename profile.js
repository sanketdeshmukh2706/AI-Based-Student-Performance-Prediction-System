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
    let branch = data.Branch;

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
    document.getElementById("Gender").innerText = data.Gender;
    document.getElementById("semester").innerText = data.Semester;
    document.getElementById("branch").innerText = data.Branch;
    document.getElementById("attandance").innerText = data.Attandance;


    document.getElementById("math").innerText = data.Maths;
    document.getElementById("ds").innerText = data.DS;
    document.getElementById("os").innerText = data.OS;
    document.getElementById("dbms").innerText = data.DBMS;
    document.getElementById("ai").innerText = data.AI;
    
    document.getElementById("FP").innerText = avg;
    document.getElementById("PP").innerText = result;
    

    document.getElementById("fname").innerText = data.Father_Name;
    document.getElementById("mname").innerText = data.Mother_Name;
    document.getElementById("DOB").innerText = data.Date_of_Birth;
    document.getElementById("BG").innerText = data.Blood_Group;

    document.getElementById("Age").innerText = data.Age;
    document.getElementById("City").innerText = data.City;
    document.getElementById("Pincode").innerText = data.Pincode;
    document.getElementById("State").innerText = data.State;
    document.getElementById("Country").innerText = data.Country;
    document.getElementById("mobile").innerText = data.Mobile_Number;
    document.getElementById("address").innerText = data.Address;
    document.getElementById("mail_ID").innerText = data.Email_ID;
    document.getElementById("Participant").innerText = data.Participant;
    document.getElementById("Game").innerText = data.Game;
    
    // CE = 318, ECE = 317, CSE = 298, IT = 292, ME = 275
    
    if(branch =="IT"){
      document.getElementById("sub1").innerText = "Data Structure";
      document.getElementById("sub2").innerText = "Operating System";
      document.getElementById("sub3").innerText = "Networking & OS";
      document.getElementById("sub4").innerText = "Database & Data";
      document.getElementById("sub5").innerText = "Data Science";
    }
    else if(branch =="CSE"){
      document.getElementById("sub1").innerText = "Data Structure";
      document.getElementById("sub2").innerText = "Operating System";
      document.getElementById("sub3").innerText = "Digital Marketing";
      document.getElementById("sub4").innerText = "AI and Modern Tech";
      document.getElementById("sub5").innerText = "Management";
    }
    else if (branch =="CE"){
      document.getElementById("sub1").innerText = "Construction & Management";
      document.getElementById("sub2").innerText = "Geotechnical Engineering";
      document.getElementById("sub3").innerText = "Water Resources & Enviromental";
      document.getElementById("sub4").innerText = "Transportation Engineering";
      document.getElementById("sub5").innerText = "Maths";
    }
    else if(branch =="ECE"){
      document.getElementById("sub1").innerText = "Machines & Power";
      document.getElementById("sub2").innerText = "Control & Electronics";
      document.getElementById("sub3").innerText = "Systems & Application";
      document.getElementById("sub4").innerText = "Engineering Mathematics";
      document.getElementById("sub5").innerText = "Engineering Drawing";
    }
    else {
      document.getElementById("sub1").innerText = "Engineering Mathematics";
      document.getElementById("sub2").innerText = "Engineering Drawing";
      document.getElementById("sub3").innerText = "Engineering Physics";
      document.getElementById("sub4").innerText = "Engineering Chemestry";
      document.getElementById("sub5").innerText = "Strength of Materials";
    }

  
  });