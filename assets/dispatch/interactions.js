(() => {
'use strict';
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const form=document.querySelector('.paper-tools');
if(form){
 const rows=[...document.querySelectorAll('.paper')], archive=document.querySelector('.paper-archive');
 const filter=()=>{const values=new FormData(form);const words=String(values.get('q')||'').toLowerCase().trim().split(/\s+/).filter(Boolean);const year=values.get('year'),kind=values.get('kind'),theme=values.get('theme');let count=0;rows.forEach(row=>{const on=(!year||row.dataset.year===year)&&(!kind||row.dataset.kind===kind)&&(!theme||row.dataset.themes.split(' ').includes(theme))&&words.every(w=>row.dataset.search.includes(w));row.hidden=!on;if(on)count++});document.querySelector('.paper-count').textContent=count===rows.length?`${count} papers`:`${count} of ${rows.length} papers`;document.querySelector('.paper-empty').hidden=count>0;if(archive){archive.hidden=![...archive.querySelectorAll('.paper')].some(p=>!p.hidden);archive.open=Boolean(words.length||year||kind||theme)}};
 form.addEventListener('input',filter);form.addEventListener('change',filter);form.addEventListener('reset',()=>requestAnimationFrame(filter));form.addEventListener('submit',e=>{e.preventDefault();filter()});
 document.querySelectorAll('[data-theme-jump]').forEach(a=>a.addEventListener('click',()=>{form.reset();form.elements.theme.value=a.dataset.themeJump;filter();document.querySelector('.paper-tools').scrollIntoView({block:'center',behavior:reduced.matches?'auto':'smooth'})}));
 document.querySelectorAll('.copy-citation').forEach(b=>b.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(b.dataset.citation);b.textContent='Citation copied';document.querySelector('.announcement').textContent='Citation copied';setTimeout(()=>{b.textContent='Copy citation'},2200)}catch{let text=b.parentElement.querySelector('textarea');if(!text){text=document.createElement('textarea');text.readOnly=true;text.value=b.dataset.citation;b.after(text)}text.focus();text.select();b.textContent='Select and copy'}}));
}
document.querySelectorAll('[data-responsive-menu]').forEach(menu=>{const narrow=matchMedia('(max-width:700px)');const set=()=>{menu.open=!narrow.matches};set();narrow.addEventListener('change',set)});
const chapterNav=document.querySelector('[data-chapters]');
if(chapterNav){
 const links=[...chapterNav.querySelectorAll('a')],panels=[...document.querySelectorAll('[data-chapter]')];
 function activate(){
  const id=location.hash.slice(1),target=document.getElementById(id);
  const chapter=target?.closest('[data-chapter]');
  const selected=chapter?.id||(id==='main'?panels.find(p=>!p.hidden)?.id:'overview')||'overview';
  document.body.classList.add('chapters-ready');
  panels.forEach(p=>{p.hidden=p.id!==selected});
  links.forEach(a=>{if(a.hash==='#'+selected)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
  if(target&&id!=='overview')requestAnimationFrame(()=>target.scrollIntoView({block:'start',behavior:'instant'}));
 }
 addEventListener('hashchange',activate);activate();
}
const pause=document.querySelector('[data-motion-toggle]'),stage=document.querySelector('.research-map');
if(pause&&stage){pause.addEventListener('click',()=>{const state=pause.getAttribute('aria-pressed')!=='true';pause.setAttribute('aria-pressed',String(state));pause.textContent=state?'Resume motion':'Pause motion';stage.classList.toggle('paused',state)});reduced.addEventListener('change',()=>stage.classList.toggle('reduced',reduced.matches));stage.classList.toggle('reduced',reduced.matches)}
const nav=[...document.querySelectorAll('nav a[href^="#"]')];if(!chapterNav&&'IntersectionObserver'in window){const obs=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)nav.forEach(a=>{if(a.hash==='#'+e.target.id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})}),{rootMargin:'-15% 0px -65% 0px'});document.querySelectorAll('main section[id]').forEach(s=>obs.observe(s))}
})();
