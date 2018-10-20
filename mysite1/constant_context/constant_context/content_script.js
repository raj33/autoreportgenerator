// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
window.onload=function(){
//alert("hiii");
var btn = document.createElement("BUTTON");
var t = document.createTextNode("CLICK ME");
btn.appendChild(t);
document.body.appendChild(btn);
//var na1=""
btn.onclick=function (){
    //alert('h2');
    if (document.getElementsByClassName('title2')[0].innerText=='Register Grievance'){
        console.log('outpur1');
        console.log(document.getElementsByClassName("form-control")[1].value);
        //var details=document.getElementsByClassName("form-control")[1].value;
        var name=document.getElementsByClassName("form-control")[3].value;
        var phone=document.getElementsByClassName("form-control")[4].value;
        //var email=document.getElementsByClassName("form-control")[5].value;
        var category=document.getElementsByClassName("form-control")[6].value;
        var type=document.getElementsByClassName("form-control")[7].value;
        //var details=document.getElementsByClassName("form-control")[8].value;
        ulbname=document.URL;
        console.log(ulbname);
        ulbname=ulbname.replace('http://','');
        ulbname=ulbname.replace('.emunicipal.ap.gov.in/pgr/grievance/thirdparty/show-reg-form?source=CCCU#','');
        ulbname=ulbname.replace('.emunicipal.ap.gov.in/pgr/grievance/thirdparty/show-reg-form?source=CCCU','');
        var theValue=name+'@'+phone+'@'+category+'@'+type+'@'+ulbname;
        localStorage.setItem('data',theValue);
        //url="http://192.168.55.23:8000/adverse/"+name+'@'+phone+'@'+category+'@'+type;
        //url=url.concat(center);
    }
    else{
      a=document.getElementsByClassName('panel-title text-center no-float')[0].innerText
      if(a.match(/successfully/gi)){
           crr=a.replace("Your grievance successfully registered with CRN : ", "")
          // crr=document.URL
           //crr=crr.replace('http://','');
           //crr=crr.replace(na1,'');
           //crr=crr.replace('.emunicipal.ap.gov.in/pgr/complaint/reg-success/','');
           g=localStorage.getItem(['data']);
           url='http://192.168.55.16:8000/adverse/'+g+'@'+crr;
           var xhttp = new XMLHttpRequest();
           xhttp.open("POST", url, true);
           xhttp.send("fnamejjjjj");
         }
        }
    }
}