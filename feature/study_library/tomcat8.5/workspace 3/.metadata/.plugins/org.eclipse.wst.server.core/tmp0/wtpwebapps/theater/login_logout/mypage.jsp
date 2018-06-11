<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>My Page</title>


</head>
<body>

<center>
<h2>환영합니다!</h2>
<p>
<hr>
<p><% 
out.println(session.getAttribute("name") + "님 환영합니다.");%>
<p>
<hr>
<h4>My Page</h4>
<ul>
<li><a href=../category/list_user.jsp>회원정보 수정</a></li>
<li><a href=../reservation/20171215_movie_timetable.jsp>애견정보 생성</a></li>
<li><a href=../reservation/reservation_result.jsp> 애견정보 수정 </a></li>
<li><a href=delete.jsp> 회원탈퇴</a></li>

</ul>

</center>

</body>
</html>