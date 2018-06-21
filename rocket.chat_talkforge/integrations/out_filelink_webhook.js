class Script {

  prepare_outgoing_request({ request }) {
    
    let files = request.data.message.attachments;
    let links = '';
    for (a of files) {
      links += 'https://talkforge.com' + a.image_url + ' ';
    }
    
    if (request.data.text.length == 0) {
      return {
        "method": "POST",   
        "url": request.url,   
        "data": {     
          "text": links,
          "bot": {
           "name": request.data.user_name,
           "image": "https://www.zoho.com/cliq/help/restapi/images/bot-custom.png"
          },
        },
        "headers": {     
          "Content-type": "application/json",
          "Authorization": "Zoho-authtoken b2dd5ea5f4919a29069910afa08c1f60"
        }
      }
    }
  }

  process_outgoing_response({ request, response }) {
  }
}