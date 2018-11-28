let menu_trigger = document.getElementById('menu_trigger');
let body = document.getElementsByTagName("body")[0];
menu_trigger.addEventListener('click', () => {
  console.log('click');
  console.log(body);
  let nav_list = document.querySelector('.nav-list');
  nav_list.classList.toggle('hide');
  body.classList.toggle('show-nav');
});
