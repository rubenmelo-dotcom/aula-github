// script.js
// Exemplo simples: alerta ao clicar em qualquer botão

document.querySelectorAll('button').forEach(btn => {
  btn.addEventListener('click', () => {
    alert('Botão clicado!');
  });
});

console.log("Primeira mensagem no console");
console.log("Segunda mensagem");