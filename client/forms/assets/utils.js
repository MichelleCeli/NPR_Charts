  
const setting = {
  local: {
    API_URL: 'http://localhost:8000/',
    mode: 'cors'
  },
  remote: {
    API_URL: 'https://game-forms-bakend.herokuapp.com/',
    mode: 'no-cors'
  }
}

const API_URL =  'https://game-forms-bakend.herokuapp.com/' 
//'http://localhost:8000/'

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data) 
    });
    return response.json(); 
  }

function getData(url = '') {
  return fetch(url, {
    method: 'POST',
    mode: 'cors'
  }).then(response => response.json())
}