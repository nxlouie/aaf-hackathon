let button = document.getElementById('clo')
let fdiv = document.getElementById('form')

let cdinput = document.createElement('div')
let clinput = document.createElement('label')
let cinput = document.createElement('input')

let ldinput = document.createElement('div')
let llinput = document.createElement('label')
let linput = document.createElement('input')

let rdinput = document.createElement('div')
let rlinput = document.createElement('label')
let rinput = document.createElement('input')

let xdinput = document.createElement('div')
let xlinput = document.createElement('label')
let xinput = document.createElement('input')

let mdinput = document.createElement('div')
let mlinput = document.createElement('label')
let minput = document.createElement('input')

let tdinput = document.createElement('div')
let tlinput = document.createElement('label')
let tinput = document.createElement('input')

let ydinput = document.createElement('div')
let ylinput = document.createElement('label')
let yinput = document.createElement('input')

clinput.innerHTML = "CNN URL: "
llinput.innerHTML = "LinkedIn URL: "
rlinput.innerHTML = "Reddit URL: "
xlinput.innerHTML = "X URL: "
mlinput.innerHTML = "NBC URL: "
tlinput.innerHTML = "TikTok URL: "
ylinput.innerHTML = "Youtube URL: "

fdiv.style.setProperty("width", "370px")
fdiv.style.setProperty("display", "block")
fdiv.style.setProperty("justify-content", "space-between")
fdiv.style.setProperty("border-style", "groove")

function caddfield(){
    fdiv.appendChild(cdinput)
    cdinput.appendChild(clinput)
    cdinput.appendChild(cinput)

    cdinput.style.setProperty("margin", "10px")
}

function laddfield(){
    fdiv.appendChild(ldinput)
    ldinput.appendChild(llinput)
    ldinput.appendChild(linput)

    ldinput.style.setProperty("display", "inline")
    ldinput.style.setProperty("justify-content", "space-between")
}

function raddfield(){
    fdiv.appendChild(rdinput)
    rdinput.appendChild(rlinput)
    rdinput.appendChild(rinput)
}

function xaddfield(){
    fdiv.appendChild(xdinput)
    xdinput.appendChild(xlinput)
    xdinput.appendChild(xinput)
}

function maddfield(){
    fdiv.appendChild(mdinput)
    mdinput.appendChild(mlinput)
    mdinput.appendChild(minput)
}

function taddfield(){
    fdiv.appendChild(tdinput)
    tdinput.appendChild(tlinput)
    tdinput.appendChild(tinput)
}

function yaddfield(){
    fdiv.appendChild(ydinput)
    ydinput.appendChild(ylinput)
    ydinput.appendChild(yinput)
}