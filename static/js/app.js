document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('input:not([type=checkbox]):not([type=file]),textarea,select').forEach(el=>{
    if(!el.classList.contains('form-control')&&!el.classList.contains('form-select')) el.classList.add(el.tagName==='SELECT'?'form-select':'form-control');
  });
  document.querySelectorAll('video').forEach(player=>{
    player.addEventListener('error',()=>console.warn('Video playback failed. Check the uploaded file format and browser codec support.'));
    if(player.dataset.authenticated==='true' && player.dataset.progressUrl){
      let lastSent=0;
      const csrf=(document.cookie.split('; ').find(row=>row.startsWith('csrftoken='))||'').split('=')[1];
      player.addEventListener('timeupdate',()=>{
        const seconds=Math.floor(player.currentTime);
        if(seconds-lastSent>=10){lastSent=seconds;const body=new URLSearchParams({seconds:String(seconds)});fetch(player.dataset.progressUrl,{method:'POST',headers:{'X-CSRFToken':csrf,'Content-Type':'application/x-www-form-urlencoded'},body,credentials:'same-origin'}).catch(()=>{});}
      });
    }
  });
});
