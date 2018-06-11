<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.sql.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>회원탈퇴화면</title>
</head>
<body>
<center>
<br><br>
    <b><font size="6" color="gray">내 정보</font></b>
    <br><br><br>
 
    <form name="deleteform" method="post" action="deleteConfirm.jsp">
    <p> 탈퇴를 원하시면 비밀번호를 한 번 더 입력해 주세요. </p>
        <table>
            <tr>
                <td>비밀번호 확인</td>
                <td><input type="password" name="password" maxlength="50"></td>
            </tr>
        </table>
        
        <br> 
        <input type="submit" value="탈퇴"/> 
        <input type="reset" value="취소">
    </form>
</center>
    
</body>
</html>