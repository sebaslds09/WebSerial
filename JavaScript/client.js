/*  Copyright 2014 Sebastian Ortiz
	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
	*/
'use strict'

function start_() {
	var inmsn = document.getElementById('inmsn');
	var form = document.getElementById('form');
	var outmsn = document.getElementById('outmsn');
	
	try {
 
		var host = "ws://localhost:9876";
		console.log("Host:", host);
	
		var s = new WebSocket(host);
	
		s.onopen = function (e) {
			console.log("Socket opened.");
		};
		
		s.onclose = function (e) {
			console.log("Socket closed.");
			window.alert("Server not detected");
			var r = confirm("Please open the server and then press Accept. If you don't have it please cancel to download it");
			if (r == true){
				location.reload(true);
			}
			else{
				window.open('http://www.aquiladescarga.com');
			}
		};

		s.onerror = function (e) {
			console.log("Socket error:", e);
		};
		
		s.onmessage = function (e) {
			outmsn.value = outmsn.value + e.data;
			outmsn.scrollTop = outmsn.scrollHeight;
		};	
	} 
	catch (ex) {
		console.log("Socket exception:", ex);
	}
 
	form.addEventListener("submit", function (e) {
		e.preventDefault();
		var inmsnV = inmsn.value;
		if(inmsnV == ''){
			window.alert("Error, empty field");
		}else{
			for(var i = 0; i < inmsnV.length; i++){
				window.setTimeout(s.send(inmsnV.charAt(i)),500);
			}
			window.setTimeout(s.send('\n'),500);
		}
	}, false)
}
