(() => {
'use strict';
const reduce=matchMedia('(prefers-reduced-motion: reduce)');
const elements=[...document.querySelectorAll('.arrival')];
if('IntersectionObserver' in window&&!reduce.matches){
 document.body.classList.add('motion-ready');
 const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('arrived');observer.unobserve(entry.target)}}),{threshold:.08,rootMargin:'0px 0px -12px 0px'});
 elements.forEach((el,i)=>{el.style.setProperty('--delay',`${i%3*65}ms`);observer.observe(el)});
}
reduce.addEventListener('change',()=>{if(reduce.matches){document.body.classList.remove('motion-ready');elements.forEach(el=>el.classList.add('arrived'))}});
const form=document.querySelector('.paper-tools');
if(form){
 const records=[...document.querySelectorAll('.paper-record')],groups=[...document.querySelectorAll('.year-group')];
 const filter=()=>{const query=form.elements.query.value.trim().toLowerCase().split(/\s+/).filter(Boolean),year=form.elements.year.value;let count=0;
 records.forEach(el=>{const match=(!year||el.dataset.year===year)&&query.every(q=>el.dataset.search.includes(q));el.hidden=!match;if(match)count++});
 groups.forEach(el=>{el.hidden=![...el.querySelectorAll('.paper-record')].some(p=>!p.hidden);if(query.length||year)el.open=true});
 document.querySelector('.search-count').textContent=`${count} ${count===1?'paper':'papers'}`;document.querySelector('.empty-search').hidden=count>0;
 };
 form.addEventListener('input',filter);form.addEventListener('change',filter);form.addEventListener('submit',e=>{e.preventDefault();filter()});
}
document.querySelectorAll('.copy-citation').forEach(button=>button.addEventListener('click',async()=>{
 try{await navigator.clipboard.writeText(button.dataset.citation);button.textContent='Citation copied';document.querySelector('.announcement').textContent='Citation copied to clipboard';setTimeout(()=>button.textContent='Copy citation',2200)}catch{let text=button.parentElement.querySelector('textarea');if(!text){text=document.createElement('textarea');text.readOnly=true;text.value=button.dataset.citation;button.after(text)}text.focus();text.select();button.textContent='Select and copy the citation'}
}));
const email=document.querySelector('.email-form');if(email)email.addEventListener('submit',e=>{
 e.preventDefault();if(!email.reportValidity())return;
 const f=new FormData(email),body=`${f.get('message')}\n\n${f.get('name')}\n${f.get('email')}`;
 const url=`mailto:haohongzh@gmail.com?subject=${encodeURIComponent(f.get('subject'))}&body=${encodeURIComponent(body)}`;
 let a=email.querySelector('.prepared-email');if(!a){a=document.createElement('a');a.className='prepared-email';a.textContent='Open the prepared email ↗';email.append(a)}a.href=url;
 document.querySelector('.announcement').textContent='Email prepared. Use the link below to open it in your mail app.';a.focus();
});
})();
