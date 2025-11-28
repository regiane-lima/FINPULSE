// Navegação
const sections = {
  dashboard: document.getElementById('section-dashboard'),
  pix: document.getElementById('section-pix'),
  recharge: document.getElementById('section-recharge')
};
document.getElementById('nav-dashboard').onclick = ()=>showSection('dashboard');
document.getElementById('nav-pix').onclick = ()=>showSection('pix');
document.getElementById('nav-recharge').onclick = ()=>showSection('recharge');
function showSection(name){ Object.values(sections).forEach(s=>s.classList.add('hidden')); sections[name].classList.remove('hidden'); }

// Saldo inicial e histórico
let balance = 1500;
const balanceEl = document.getElementById('balance');
const lastPix = document.getElementById('last-pix');

// Feedback deluxe
function showFeedbackCard(el,message,type){
  el.innerText=message;
  el.className=feedback-card ${type} show;
  setTimeout(()=>el.className='feedback-card',1500);
}

// Adicionar transação com animação
function addTransaction(type, amount){
  const li = document.createElement('li');
  let icon,text,cssClass;
  switch(type){
    case 'sent': icon='fas fa-paper-plane'; text=PIX R$${amount} enviado; cssClass='success'; navigator.vibrate([100,50,100]); break;
    case 'received': icon='fas fa-download'; text=PIX R$${amount} recebido; cssClass='received'; navigator.vibrate([80,50,80]); break;
    case 'error': icon='fas fa-exclamation-triangle'; text=Erro PIX R$${amount}; cssClass='error'; navigator.vibrate([200,100,200]); break;
  }
  li.innerHTML=<i class="${icon}"></i>${text};
  li.classList.add(cssClass);
  li.style.transform="scale(0.5)";
  lastPix.prepend(li);
  setTimeout(()=>li.style.transform="scale(1)",50);
}

// PIX
document.getElementById('send-pix').onclick = ()=>{
  const amount = Number(document.getElementById('pix-amount').value);
  const feedback = document.getElementById('pix-feedback');
  if(amount <=0 || amount>balance){ showFeedbackCard(feedback,"Erro: valor inválido!","error"); addTransaction('error',amount); return; }
  showFeedbackCard(feedback,"Processando PIX...","success");
  setTimeout(()=>{
    balance -= amount;
    balanceEl.innerText=R$ ${balance};
    addTransaction('sent',amount);
    showFeedbackCard(feedback,"PIX enviado com sucesso!","success");
    updateBalanceChart();
  },1200);
};

// Recarga
document.getElementById('do-recharge').onclick = ()=>{
  const amount = Number(document.getElementById('recharge-amount').value);
  const feedback = document.getElementById('recharge-feedback');
  if(amount <=0){ showFeedbackCard(feedback,"Erro: valor inválido!","error"); return; }
  balance += amount;
  balanceEl.innerText=R$ ${balance};
  addTransaction('received',amount);
  showFeedbackCard(feedback,"Recarga realizada com sucesso!","success");
  updateBalanceChart();
};

// Gráfico de saldo (canvas)
const canvas = document.getElementById('balance-chart');
const ctx = canvas.getContext('2d');
let balanceHistory = [balance];
function updateBalanceChart(){
  balanceHistory.push(balance);
  if(balanceHistory.length>20) balanceHistory.shift();
  ctx.clearRect(0,0,canvas.width,canvas.height);
  ctx.beginPath();
  ctx.moveTo(0,canvas.height-balanceHistory[0]/10);
  for(let i=1;i<balanceHistory.length;i++){
    ctx.lineTo(i*5,canvas.height-balanceHistory[i]/10);
  }
  ctx.strokeStyle="#fff";
  ctx.lineWidth=2;
  ctx.stroke();
}
updateBalanceChart();
