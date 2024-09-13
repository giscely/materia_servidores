let cor_1=document.getElementById('red')
let cor_2=document.getElementById('green')
let cor_3=document.getElementById('yellow')
let cor_4=document.getElementById('pink')
let cor_5=document.getElementById('blue')
let cor_6=document.getElementById('white')
let conteudo=document.getElementById('box')

cor_1.addEventListener('click',()=>{
    conteudo.style.backgroundColor = 'red'
})
cor_2.addEventListener('click',()=>{
    conteudo.style.backgroundColor = 'green'
})
cor_3.addEventListener('click',()=>{
    conteudo.style.backgroundColor = 'yellow'
})
cor_4.addEventListener('click',()=>{
    conteudo.style.backgroundColor = 'pink'
})
cor_5.addEventListener('click',()=>{
    conteudo.style.backgroundColor = 'blue'
})
cor_6.addEventListener('click',()=>{
    conteudo.style.backgroundColor = 'white'
})