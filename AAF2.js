let button = document.getElementById('clo')
let fdiv = document.getElementById('form')

let dinput = document.createElement('div')
let clinput = document.createElement('label')
let cinput = document.createElement('input')

let llinput = document.createElement('label')
let linput = document.createElement('input')

let rlinput = document.createElement('label')
let rinput = document.createElement('input')

let xlinput = document.createElement('label')
let xinput = document.createElement('input')

let mlinput = document.createElement('label')
let minput = document.createElement('input')

let tlinput = document.createElement('label')
let tinput = document.createElement('input')

let ylinput = document.createElement('label')
let yinput = document.createElement('input')

clinput.innerHTML = "CNN URL: "
llinput.innerHTML = "LinkedIn URL: "
rlinput.innerHTML = "Reddit URL: "
xlinput.innerHTML = "X URL: "
mlinput.innerHTML = "NBC URL: "
tlinput.innerHTML = "TikTok URL: "
ylinput.innerHTML = "Youtube URL: "

function caddfield(){
    fdiv.appendChild(dinput)
    dinput.appendChild(clinput)
    dinput.appendChild(cinput)
}

function laddfield(){
    fdiv.appendChild(dinput)
    dinput.appendChild(llinput)
    dinput.appendChild(llinput)
}

function raddfield(){
    fdiv.appendChild(dinput)
    dinput.appendChild(rlinput)
    dinput.appendChild(rinput)
}

function xaddfield(){
    fdiv.appendChild(dinput)
    dinput.appendChild(xlinput)
    dinput.appendChild(xinput)
}

function maddfield(){
    fdiv.appendChild(dinput)
    dinput.appendChild(mlinput)
    dinput.appendChild(minput)
}

function taddfield(){
    fdiv.appendChild(dinput)
    dinput.appendChild(tlinput)
    dinput.appendChild(tinput)
}

function yaddfield(){
    fdiv.appendChild(dinput)
    dinput.appendChild(ylinput)
    dinput.appendChild(yinput)
}