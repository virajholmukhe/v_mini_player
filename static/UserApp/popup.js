console.log("popup.js is running")

msg = document.getElementById("msg").value
ons.notification.toast(msg, { timeout: 2000, animation: 'fall' })