fetch("/api/student")
.then(res => res.json())
.then(data => {

if(data.error){
alert(data.error)
return
}

let marks = [
Number(data.Maths),
Number(data.DS),
Number(data.OS),
Number(data.DBMS),
Number(data.AI)
]

let maxMarks = Math.max(...marks)
let minMarks = Math.min(...marks)
let avg = marks.reduce((a,b)=>a+b,0)/marks.length

document.getElementById("max").innerText = maxMarks
document.getElementById("min").innerText = minMarks
document.getElementById("avg").innerText = avg.toFixed(2)

let progressBars = document.querySelectorAll(".progress div")

progressBars[0].style.width = maxMarks + "%"
progressBars[1].style.width = minMarks + "%"
progressBars[2].style.width = avg + "%"

})