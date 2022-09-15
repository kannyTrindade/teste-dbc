(function(){
    var menu = document.querySelectorAll(".dropdown-toggle");
    var menuBtn = document.querySelector(".menuBtn");
    var overlayMenu = document.querySelector(".overlay");
    overlayMenu.addEventListener('click',function(e){
      toggleMenu(menuBtn);
    });


    function openDropdown(event){
      event.target.parentNode.classList.add("open"); // Adicioona classe open para exibir as opções do dropdown
    }
  
    function resetDropdowns(){
      var element = document.querySelector(".dropdown.open"); 
      if(element){ element.classList.remove("open"); }
      // Seleciona o elemento dropdown e verifica se o mesmo já está aberto, se ja estiver, remove a classe open
    }
  
    function dropdownHandler(){
      resetDropdowns();
      document.removeEventListener('click', dropdownHandler , false);
    };
  
    if(menu.length>0){
        menu.forEach(el=>{
        el.addEventListener('click',function(e){
          var isActive = e.target.parentNode.classList.contains("open");
          resetDropdowns();
          if (isActive) {
            return;
          }
          e.stopPropagation();
          e.preventDefault();
          openDropdown(e);
          document.addEventListener('click', dropdownHandler, false); //add document click listener to close dropdown on outside click
        }, false);
      })
    }

    var ul = document.querySelector('.according-list');
    ul.addEventListener('click', function(e){        
        if (e.target && e.target.nodeName == 'H4') {
            e.target.classList.toggle('active');
        }
    });

    
  
  })()
  
  function inputToggle(x) {
    document.getElementById("accountAccess").reset();
    x = String(x);
    var inputs = document.querySelectorAll(".inputToggle");
    inputs.forEach(element => {
        element.classList.add("hidden");
        var texto = element.id;
        if( texto == x){
            element.classList.remove("hidden");
        }
    });
  }

  function toggleMenu(x) {
    x.classList.toggle("change");
    var menu = document.getElementById("offscreenMenu");
    var checkbox = document.getElementById("chkMenu");
    var bodyElem = document.getElementsByTagName('body')[0];
    bodyElem.classList.toggle("open-menu");
    menu.classList.toggle("closed");
    menu.classList.toggle("open");
    checkbox.checked = !checkbox.checked;
    var h4s = document.querySelectorAll('h4');
    for (var i = 0; i < h4s.length; i++) {
      h4s[i].classList.remove('active');
    }
  }


  function validateOnlyNumbers(evt) {
    var theEvent = evt || window.event;
  
    // Handle paste
    if (theEvent.type === 'paste') {
        key = event.clipboardData.getData('text/plain');
    } else {
    // Handle key press
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    }
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
      theEvent.returnValue = false;
      if(theEvent.preventDefault) theEvent.preventDefault();
    }
  }