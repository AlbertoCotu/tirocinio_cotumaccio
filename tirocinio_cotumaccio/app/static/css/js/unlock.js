$("#gender").on("change",function(){
  var sel="";
  if($(this).val() == "Female"){
    sel=' <option>Select Your Name</option>';
       sel+=' <option value="female1">Female 1</option>'
        sel+='<option value="female2">Female 2</option>'
   
    }else{// no other if since you have only two options male/female
     sel= '<option>Select Your Name</option>';
       sel+= '<option value="Male1">Male 1</option>';
       sel+= '<option value="Male2">Male 2</option>';
      }
   $("#name").html(sel);
  
  });