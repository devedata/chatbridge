class Script {
  prepare_outgoing_request({ request }) {
    // console.log('=========');
    // console.log(JSON.stringify(request, null, 2));
    
    let message_text = request.data.text;
    
    if (message_text.length > 0) {
      return {
        "method": "POST",   
        "url": request.url,   
        "data": {     
          "text": message_text,
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