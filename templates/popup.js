const button=document.querySelector('.btn');
const summary=document.querySelector('.summary');
//console.log('here');
button.addEventListener('click',()=>{
    //console.log('here');
    button.classList.add('activebtn');
    summary.classList.add('active');
    //chrome.runtime.sendMessage({message:'generate'},res=>summary.innerHTML=res);
    //console.log("message sent from popup");
    var videourl="https://cors-anywhere.herokuapp.com/";
      // chrome.tabs.onActivated.addListener(tab=>{
      //   chrome.tabs.get(tab.tabId,current_tab_info=>{
      //     videourl=current_tab_info.url;
      //   })
      // });
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      videourl+=tabs[0].url;
      chrome.tabs.sendMessage(tabs[0].id, {message: "generate", url:videourl}, function(response) {
        summary.innerHTML=response.message;
      });
    });
})