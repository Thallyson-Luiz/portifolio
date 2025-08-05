// estilizacao do carrosel de conhecimentos

const container = document.getElementById('cardsContainer');

let isDown = false;
let startX;
let scrollLeft;

container.addEventListener('mousedown', (e) => {
  isDown = true;
  container.classList.add('active');
  startX = e.pageX - container.offsetLeft;
  scrollLeft = container.scrollLeft;
});

container.addEventListener('mouseleave', () => {
  isDown = false;
  container.classList.remove('active');
});

container.addEventListener('mouseup', () => {
  isDown = false;
  container.classList.remove('active');
});

container.addEventListener('mousemove', (e) => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - container.offsetLeft;
  const walk = (x - startX) * 1; // fator de velocidade
  container.scrollLeft = scrollLeft - walk;
});


// estilização das perguntas e repostas acordion

const a_acoding = document.querySelectorAll('.a-acoding');
const description = document.querySelectorAll('.acoding-description');
const acoding = document.querySelectorAll('.acoding');

a_acoding.forEach((item, index) => {
    item.addEventListener('click', () => {
        acoding[index].classList.toggle('active');
    });
});

// estilizacao do carrosel de tecnologias 

const container2 = document.getElementById('container-cards');

let isDown2 = false;
let startX2;
let scrollLeft2;

container2.addEventListener('mousedown', (e) => {
  isDown2 = true;
  container2.classList.add('active');
  startX2 = e.pageX - container2.offsetLeft;
  scrollLeft2 = container2.scrollLeft;
});

container2.addEventListener('mouseleave', () => {
  isDown2 = false;
  container2.classList.remove('active');
});

container2.addEventListener('mouseup', () => {
  isDown2 = false;
  container2.classList.remove('active');
});

container2.addEventListener('mousemove', (e) => {
  if (!isDown2) return;
  e.preventDefault();
  const x = e.pageX - container2.offsetLeft;
  const walk = (x - startX2) * 1;
  container2.scrollLeft = scrollLeft2 - walk;
});

// estilização das setas do carrosel de tecnologias

const seta1 = document.querySelector('.seta1');
const seta2 = document.querySelector('.seta2');

seta1.addEventListener('click', () => {
    container2.scrollBy({
        left: -500,
        behavior: 'smooth'
    })
});

seta2.addEventListener('click', () => {
    container2.scrollBy({
        left: 500,
        behavior: 'smooth'
    })
});

const BURGER = document.getElementById('burger-menu');
const NAV = document.querySelector('.menu-navegador');

BURGER.addEventListener('click', () => {
  NAV.classList.toggle('activeburger');
})