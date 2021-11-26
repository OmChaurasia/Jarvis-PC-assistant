var speechRecognition = window.webkitSpeechRecognition

var recongnition = new speechRecognition()

var textbox = document.getElementById('textbox')

var board = document.getElementById('board')

var content = ''
var html=""
recongnition.continuous = true
// console.log(recongnition)
var startrecord = document.getElementById('start-record')
i=0

// recongnition start events

recongnition.onstart =()=>{
    board.innerHTML="Voice Recongnition is ON"
    
}

recongnition.onspeechend  =()=>{
    board.innerHTML ="No Activity"
    content= content.slice(0, content.length/2)
    html= textbox.innerHTML+content
    textbox.innerHTML= html+" "
    content=""
}
recongnition.onerror = (e)=>{
    board.innerHTML ="Try Again"+e.error
    console.log(e)
}

recongnition.onresult =(e)=>{

    var current= e.resultIndex;
    var transcript= e.results[current][0].transcript
    content+= transcript

    
}


startrecord.addEventListener("click", function(){
    if (content.length){
        content += ""
    }
    recongnition.start()
});




// ajax request 

var form = document.getElementById("myForm")

form.addEventListener('submit',function(e){
    textbox=document.getElementById('textbox').value
    data={
        "textbox" : textbox
    }
    console.log(data)
    e.preventDefault()
    fetch("/process",
    {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
          }
    })
    .then(response => response.json())
    .then((data) => {
        console.log(data)
        document.getElementsByClassName("box2")[0].innerHTML=data.Ans
        document.getElementsByClassName("box1")[0].innerHTML=textbox
        textbox=document.getElementById('textbox').value=""

        speech= new Audio(data.file)
        speech.play()
    }
    
    ).catch(e=> alert("erre"))
})