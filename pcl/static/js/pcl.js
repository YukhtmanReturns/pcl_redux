
function submitAjaxForm( e, u, d, t, callback, callbackError ) {
	
	if( e != null )
        e.preventDefault(); // preventing default click action

	// alert( d );
	
    $.ajax({
        url: u,
        type: t,
        data: d,
        success: function( data ) {

        	// alert( data );
        	if( callback != null ) callback( data );
            
        }, error: function(){
            // alert('error');
        	if( callbackError != null ) callbackError();
        },
    })
}	

	


$(document).ready( function() {
	
	
	bootbox.animate( false );
	
	
	
    $(".qUp,.qDown").click( function(e) {
    	
        var row = $(this).parents("tr:first");
        
        lid = $(this).data('pid');
        qid = $(this).data('qid');
        
        
        d = "lid=" + lid + "&qid=" + qid;
       	 
        if ($(this).is(".qUp")) {
            row.insertBefore( row.prev() );
            d += "&dir=up";        
        } else {
            row.insertAfter( row.next() );
            d += "&dir=dn";
        }
        
        submitAjaxForm( e,
		          	    '/user/list/question/reorder/', 
		  		  		d,
		  		  		"post",
		  		  		function(data) {
	  			      		// alert( data );
  				  	    }, 
  				  	    null );
    
    });
});

	
function delList(e) {
	
  listId = $(this).data('lid');
  
  bootbox.confirm("Are you sure you want to delete this list?", function( result ) {
  
	  if( !result ) return;
	  
      submitAjaxForm( e, '/user/list/del/', 
			  		  "id=" + listId,
			  		  "post",
			  		  function(data) {
					  	  $('#list' + listId ).hide( "slow" );
		  			  }, 
		  			  null );
	      
	  } );
}	





function resetListForPID( pid ) {

	var items = $( ".procID" + pid );
	
	// alert( pid );
	
	var qIDs = [items.size()];
	qIDs[0] = ' ';  // the weirdness
	
	var index = 0;
	items.each(
	        function(intIndex) {

	        	if( $(this).data('gone') === 'yes' ) {
//	        		alert( "skipped " + intIndex );
	        		return;
	        	}
	        	
	        	qIDs[index] = $(this).data('qid');
	            index++;
	        });
	
	l = $.trim( qIDs.join(" ") );
	
	// alert( l );
	
	$( "#saveDataList" ).data("list", l );
	$( "#resultDetails" + pid ).data("list", l );
	
}



var undoDelList = [];


function undoDelQuestion() {

	if( undoDelList.length == 0 ) {
		return false;
	}
	
	n = undoDelList.pop();
	
	$( n ).removeData("gone" );
	$( n ).show( 'slow' );

	if( undoDelList.length == 0 ) {
		$('.undoDelQ').hide();
	}

    resetListForPID( pid );
	
	return true;
}
	
function delQuestion(e) {

  lid = $(this).data('lid');
  
  qid = $(this).data('qid');
  pid = $(this).data('pid');

  n = '#quest';
  
  if( lid == "" ) {
	  n += pid;
  } else {
	  n += lid;
  }
  
  n = n + "_" + qid 
  
  $( n ).data("gone", 'yes' );
  $( n ).hide( "slow" ); //.remove();
  
  undoDelList.push( n );
  $('.undoDelQ').show();
  
  
  resetListForPID( pid );
  
  if( lid == "" ) return;
  
  
  d = "lid=" + lid + "&qid=" + qid;
  
  submitAjaxForm( e,
		          '/user/list/question/del/', 
		  		  d,
		  		  "post",
		  		  function(data) {
	  			      // $('#quest' + lid + "_" + qid ).hide( "slow" );
	  
	  				  // doing this outside now
	  
  				  },
  				  null );  
}



function editList(e) {

	lid = $(this).data('lid');
	
	bootbox.prompt("Enter new question:", function( lbl ) {
		
		if (lbl == null)
			return;
	
		d = "lid=" + lid + "&lbl=" + encodeURI( lbl );
		// alert( d );
	
		submitAjaxForm(e, 
				'/user/list/question/add/', 
				d, 
				"post", 
				function( data ) {
					// alert("Added question!" + data);
					$('#list' + lid ).html( data );
				},
				null );
		
	} );
}


function shareList(e) {

	
	
	hk = $(this).data('hk');

	u = "patientschecklist.com/share/" + hk + "/";
	
	$('#sendListLink').html( u );
	
	$('#sendListLink').attr( 'href',  "http://" + u );
	
	$('#sendListHK').val( hk );

	$('#modalSendList').modal('show');	  				      

}
	
$(function() {

	$('.delList').on('click', delList);
	$('.editList').on('click', editList);

	$('.shareList').on('click', shareList);
	
	$('.btnStarIt').on('click', btnStarIt );
	$('.delQuestion').on('click', delQuestion);
	
	
} );



	
	
$(function(){

    $('#modalSignup').on('shown', function () {
    	
        // clear input fields
    	$('#signupEmail').val("");
    	$('#signupPwd').val("");
    	$('#signupCpwd').val("");
    	
    	$('#signupEmail').focus();

    })
	
    $('#modalContact').on('shown', function () {
    	
        // clear input fields
    	$('#txt').val("");
    	$('#txt').focus();
    })
	

    $('#modalLS').on('focusin', function (e) {
            // stop focusin competition war.
            e.stopPropagation();
        });
    
    $('#modalLS').on('shown', function () {
    	
        // clear input fields
    	$('#loginEmailLS').val("");
    	$('#loginPwdLS').val("");
    	$('#loginEmailLS').focus();
    })
    
    

    
    function btnLoginCallback( data ) {
    	
		if( data == "OK" ) {
			// window.location = window.location;
			window.location = "/";
			
		} else {
			// error handling
			
			bootbox.dialog("Wrong username or password.", [
            {
			    "label" : "I forgot my password!",
			    "class" : "btn-danger",
			    "callback": function() {
			        window.location = "/user/forgot/";
			    }
			}, {
			    "label" : "Let's try again.",
			    "class" : "btn",
			}]);
			
			return;
			
			
			
			
			
			$('#modalYesNoHeader').html( "Wrong Username or Password!");
			$('#modalYesNoBody').html  ( "Username and password didn't match.");

			$('#modalYesNoClose').html ( "Try again");
			
			$('#modalYesNoAction').attr( "class", "btn btn-danger" );
			$('#modalYesNoAction').html( "I forgot my password");
				
				$('#modalYesNoAction').on( 'click', function(e) {
					
					window.location = '/user/forgot/';
					$('#modalYesNo').modal('hide');
				})
				
				$('#modalYesNo').modal('show');	  				      
		      

		}
   	}
	
	
   	function btnLogin(e) {
   		
   		if( $("#formLogin").valid() == false ) {
   			return;
   		}
   		
   		d = $("#formLogin").serialize();
   		
   		   		
   		submitAjaxForm( e, 
   						'/user/login/', 
   						d,
   						"post",
   						function(data) {
   			
   							$("#containerNavbar").html( data.navbar );
   							$("#loginMsg").show();
   							$("#containerMsg").hide();
   							
   						},
   						function() {
   							bootbox.dialog("Wrong username or password.", [
                                        {
                            			    "label" : "I forgot my password!",
                            			    "class" : "btn-danger",
                            			    "callback": function() {
                            			        window.location = "/user/forgot/";
                            			    }
                            			}, {
                            			    "label" : "Let's try again.",
                            			    "class" : "btn",
                            			}]);
                            			
                            			return;
   							
   						});
   	}
  	

   	
   	
   	
   	function modalLSbtnSubmitLogin(e) {
   		
   		d = $("#modalLSformLogin").serialize();
   		   		
   		submitAjaxForm( e, 
   						'/user/login/', 
   						d,
   						"post",
   						function(data) {
   			
   							$("#containerNavbar").html( data.navbar );

   							$("#modalLS").modal('hide');   							
   							
   							$("#modalLS").trigger('pcl-loggedin');
   							
   							
   						},
   						function() {
   							bootbox.alert("Wrong username or password." );   							
   						});
   	}

   	
   	

   	
   	function btnSignupCallback( data ) {

   		// alert( data );
   		
   		bootbox.alert( "Thank you for signing up!" );
   		
   		window.location = "/";
   		
   		return;
   		
   		
   		
   		switch( data ) {
   			
   			case "OK":  	window.location = "/";
   							break;
   							
   			case "DUPE": { 
   							$('#signUpError').show('');

   							break;
   			}
   							
   			case "FAIL":    alert( "An error occured, please try again later." );
							break;
   		}	
    }
   	

   	function btnSignup(e){

   		if( $("#formSignup").valid() == false ) {
   			return;
   		} 
   		
   		submitAjaxForm( e, 
   						'/user/signup/', 
   						$("#formSignup").serialize(),
   						"post",
   						btnSignupCallback,
   						function(e) {
   							$('#signUpError').show('');
   						} );
   	}   		
  	

   	function btnSignupCallbackLS( data ) {

   		//alert( data );
   		
		$("#containerNavbar").html( data.navbar );

		$("#modalLS").modal('hide');
		
		// bootbox.alert( "You signed up successfully!" );
		
		$("#modalLS").trigger('pcl-loggedin');
    }
   	
   	
   	
   	
   	function btnSignupLS(e){

   		/*
   		if( $("#formSignupLS").valid() == false ) {
   			return;
   		} 
   		*/
   		
   		submitAjaxForm( e, 
   						'/user/signup/', 
   						$("#formSignupLS").serialize(),
   						"post",
   						btnSignupCallbackLS,
   						function(d) {
   			
   							alert( d );
   		} );
   	}   		

	
  	
   	function btnContactSend(e){
   		
        e.preventDefault(); // preventing default click action

        submitAjaxForm( e, 
        				'/contact/send/', 
        				$("#formContact").serialize(),
        				"post",
        				null,
        				null );
        
        bootbox.alert( "Thank you for your feedback, we'll be in touch with you!")
		$("#modalContact").modal('hide');
        
    }
        
   	
   	
   	function btnSendList(e){
   		
        e.preventDefault(); // preventing default click action

        submitAjaxForm( e, 
        				'/user/list/send/', 
        				$("#formSendList").serialize(),
        				"post",
        				null,
        				null );
        
        bootbox.alert( "Checklist successfully shared!")
		$("#modalSendList").modal('hide');
        
    }

   	
   	
   	
   	$('#btnLogin'      ).on('click', btnLogin       );
	$('#btnSignup'     ).on('click', btnSignup      ); 
	$('#btnContactSend').on('click', btnContactSend ); 

	$('#btnSendList').on('click', btnSendList ); 
        

	$('#modalLSbtnSubmitSignup' ).on('click', btnSignupLS    ); 

	
	
	
	$('#modalLSbtnSubmitLogin'  ).on('click', modalLSbtnSubmitLogin );

})








function saveList(e) {
  
	pid  = $(this).data('pid');
	list = $( '#resultDetails' + pid ).data( 'list');
	
	data = "qs=" + encodeURI( list );
	
	showModalChecklist( data ); 
}




function showModalChecklist( data ) {

    $('#modalChecklist').modal('show');
    
	submitAjaxForm( null,
		        '/quick-list/',
		        data,
		        "post",
		    	function( data ) {
	      
	            	$('#modalChecklistBody').html( data );
				},
				null );
}



function saveListForUser(e, idName ) {

	if( idName == null ) {	
		idName  = '#resultDetails' + $(this).data('pid');
	}
	
	list = $.trim( $( idName ).data( 'list') );
	// alert( list );
	
	if( list.length == 0 ) {
	
		bootbox.alert("List is empty, please search again." );   							
		return;
	}
	
	
	bootbox.prompt("Enter new list name:", function( lbl ) {
		
		  if (lbl == null)
			  return;

  		  var name = lbl;

		  submitAjaxForm( e,
				  		  '/user/list/add/',
				  		  "l=" + encodeURI( list ) + "&n=" + encodeURI( name ),
				  		  "post",
				  		  function( data ){
			                  // ajax callback
			  				      
			  
									$('#modalYesNoHeader').html( "Success!");
									$('#modalYesNoBody').html  ( "Successfully saved the list.");
		
									$('#modalYesNoAction').attr( "class", "btn btn-primary" );
									$('#modalYesNoAction').html( "Go to My Checklists");
			  						
			  						$('#modalYesNoAction').on( 'click', function(e) {
			  							
			  							u = '/user/lists/#anchor-list' + data.listID;
			  							
			  							window.location = u;
			  							$('#modalYesNo').modal('hide');
			  						})
			  						
			  						$('#modalYesNo').modal('show');	  				      
			  				      
		      				  },
		      				  null );
			
		})
		
	      
}













function btnStarIt (e) {
		
	    pid  = $(this).data('pid');
	    qid  = $(this).data('qid');
		

		
		submitAjaxForm( null,
		        '/user/loggedin/',
		        "",
		        "post",
		    	function( data ) {
		
					voteUpQuestion( e, pid, qid );
				},
				function() {
					askLoginSignup( e, null );
				} );
		
}


function voteUpQuestion(e, pid, qid ) {
	
    // alert("Star it " + pid + " " + qid );
    submitAjaxForm( e,
  		  		    '/question/star/',
  		  		    "pid=" + pid + "&qid=" + qid,
  		  		    "post",
  		  		    function( data ){
		                  
		              	n = "#btnStar" + qid + "_" + pid;
		                  
		                if( data == "0" ) {
		                	// not voted up
	                	    $( n ).attr('class', "btn pull-right" );              	  
		                } else if( data == "1" ) {
		                	$( n ).attr('class', "btn btn-success pull-right" );              	  
			            }  
        			},
        			null );
			
}



function askLoginSignup( e, extraFunc ) {
	
	
	if( extraFunc ) {
		
		$("#modalNotLoggedIn").on( 'hide', extraFunc );		
	}  
	
	$("#modalLS").modal( {keyboard: true} )
	
}





$( function() {

	// $('.saveList').on('click', saveList );  		
})

  
      
