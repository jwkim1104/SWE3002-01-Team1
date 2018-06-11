<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.sql.*"%>
<% request.setCharacterEncoding("utf-8"); %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>회원가입</title>

</head>
<body>


<script>
function writeCheck(){
	var form = document.userForm;
	var emailExp = /[0-9a-zA-Z][_0-9a-zA-Z-]*@[_0-9a-zA-Z-]+(\.[_0-9a-zA-Z-]+){1,2}$/;
	var phoneExp = /^[0-9]+$/;

	if(!form.name.value){
		alert("이름을 입력해 주세요!");
		form.name.focus();
		return;
	}
	if(!form.id.value){
		alert("ID를 입력해 주세요!");
		form.id.focus();
		return;
	}
	if (!form.email.value.match(emailExp)) {
		alert("email형식이 올바르지 않습니다. 다시 확인해 주세요!");
		form.id.focus();
		return;
	}


	if(!form.pass1.value){
		alert("비밀번호를 입력해 주세요!");
		form.pass1.focus();
		return;
	}
	if(form.pass1.value != form.pass2.value){
		alert("비밀번호가 일치하지 않습니다. 다시 확인해 주세요!");
		form.pass2.focus();
		return;
	}
	if(!form.phone.value){
		alert("휴대폰 번호를 입력해 주세요!");
		form.phone.focus();
		return;
	}
	if (!form.phone.value.match(phoneExp)) {
		alert("휴대폰 번호 형식이 올바르지 않습니다. 숫자 입력해 주세요!");
		form.phone.focus();
		return;
	}
	if(form.use.value == "no"){
		alert("이용약관에 동의해 주세요!");
		form.use.focus();
		return;
	}
	if(form.info.value == "no"){
		alert("정보수집에 동의해 주세요!");
		form.info.focus();
		return;
	}

	form.submit();
}
</script>
<center>
<h1>SIGN UP</h1>
	<h4>회원정보를 입력하세요.</h4>
	<form name=userForm method=post action=regConform.jsp>
		<table>
			<tr>
				<td> 이름 </td>
				<td> <input type=text name="name"></td>
			</tr>
			<tr>
				<td> ID </td>
				<td> <input type=text name="id"></td>
			</tr>
			<tr>
				<td> email </td>
				<td> <input type=text name="email"></td>
			</tr>
			<tr>
				<td> 암호 </td>
				<td> <input type=password name="pass1"></td>
			</tr>
			<tr>
				<td> 암호 확인 </td>
				<td> <input type=password name="pass2"></td>
			</tr>
			<tr>
				<td> 휴대폰번호 </td>
				<td> <input type=text name="phone"></td>
			</tr>
			<tr>
				<td> Feedbap 이용약관<b>(필수)</b> </td>
				<td> <input type="radio" name="use" value="ok">동의 &nbsp;
				<input type="radio" name="use" value="no">비동의</td>
			</tr>
			<tr>
				<td>Feedbap 정보수집<b>(필수)</b> </td>
				<td> <input type="radio" name="info" value="ok">동의 &nbsp;
				 <input type="radio" name="info" value="no">비동의</td>
			</tr>
			<tr>
				<td> 프로모션 알림 메일 수신(선택) </td>
				<td> <input type="radio" name="pro" value="ok">동의 &nbsp;
				<input type="radio" name="pro" value="no">비동의</td>
			</tr>
			<tr>
				<td colspan=2>
				<center>
				<input type="button" onclick="writeCheck();" value="확인">
				<input type=reset value="취소">
				</center>
				</td>
			</tr>
		</table>
	</form>
	<p>
	<hr>
	<a href=show.jsp> <font color=blue>내용저장 확인</font></a>


</center>
</body>
</html>