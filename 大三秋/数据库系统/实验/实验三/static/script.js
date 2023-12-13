function openForm(formId) {
    document.getElementById(formId).style.display = "block";
}

function closeForm(formId) {
    document.getElementById(formId).style.display = "none";
}

function addStudent() {
  // 获取表单数据
  var sno = document.getElementById("sno").value;
  var sname = document.getElementById("sname").value;
  var ssex = document.getElementById("ssex").value;
  var sage = document.getElementById("sage").value;
  var sdept = document.getElementById("sdept").value;

  // 创建一个XMLHttpRequest对象
  var xhr = new XMLHttpRequest();

  // 配置请求
  xhr.open("POST", "/addStudent", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  // 处理响应
xhr.onload = function() {
  if (xhr.status === 200) {
    var response = JSON.parse(xhr.responseText);
    alert(response.result);
    location.reload(); // 刷新页面
  } else {
    alert('Error');
  }
};


  // 发送请求
  xhr.send("sno=" + sno + "&sname=" + sname + "&ssex=" + ssex + "&sage=" + sage + "&sdept=" + sdept);
}

function deleteStudent(sno) {
    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 配置请求
    xhr.open("POST", "/deleteStudent", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // 处理响应
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.result);
            location.reload(); // 刷新页面
        } else {
            alert('Error');
        }
    };
}

function updateStudent() {
    // 获取表单数据
    var sno = document.getElementById("sno").value;
    var sname = document.getElementById("sname").value;
    var ssex = document.getElementById("ssex").value;
    var sage = document.getElementById("sage").value;
    var sdept = document.getElementById("sdept").value;

    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 配置请求
    xhr.open("POST", "/updateStudent", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // 处理响应
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.result);
            location.reload(); // 刷新页面
        } else {
            alert('Error');
        }
    };

    // 发送请求
    xhr.send("sno=" + sno + "&sname=" + sname + "&ssex=" + ssex + "&sage=" + sage + "&sdept=" + sdept);
}

function addCourse(){
    // 获取表单数据
    var cno = document.getElementById("cno").value;
    var cname = document.getElementById("cname").value;
    var credit = document.getElementById("credit").value;

    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 配置请求
    xhr.open("POST", "/addCourse", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // 处理响应
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.result);
            location.reload(); // 刷新页面
        } else {
            alert('Error');
        }
    };

    // 发送请求
    xhr.send("cno=" + cno + "&cname=" + cname + "&credit=" + credit);
}

function deleteCourse(cno) {
    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 配置请求
    xhr.open("POST", "/deleteCourse", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // 处理响应
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.result);
            location.reload(); // 刷新页面
        } else {
            alert('Error');
        }
    };
}

function updateCourse() {
    // 获取表单数据
    var cno = document.getElementById("cno").value;
    var cname = document.getElementById("cname").value;
    var credit = document.getElementById("credit").value;

    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 配置请求
    xhr.open("POST", "/updateCourse", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // 处理响应
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.result);
            location.reload(); // 刷新页面
        } else {
            alert('Error');
        }
    };

    // 发送请求
    xhr.send("cno=" + cno + "&cname=" + cname + "&credit=" + credit);
}

function addSC(){
    // 获取表单数据
    var sno = document.getElementById("sno").value;
    var cno = document.getElementById("cno").value;
    var grade = document.getElementById("grade").value;

    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 配置请求
    xhr.open("POST", "/addSC", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // 处理响应
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.result);
            location.reload(); // 刷新页面
        } else {
            alert('Error');
        }
    };

    // 发送请求
    xhr.send("sno=" + sno + "&cno=" + cno + "&grade=" + grade);
}

function deleteSC(sno, cno) {
    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 配置请求
    xhr.open("POST", "/deleteSC", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // 处理响应
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.result);
            location.reload(); // 刷新页面
        } else {
            alert('Error');
        }
    };
}

function updateSC() {
    // 获取表单数据
    var sno = document.getElementById("sno").value;
    var cno = document.getElementById("cno").value;
    var grade = document.getElementById("grade").value;

    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 配置请求
    xhr.open("POST", "/updateSC", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // 处理响应
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.result);
            location.reload(); // 刷新页面
        } else {
            alert('Error');
        }
    };

    // 发送请求
    xhr.send("sno=" + sno + "&cno=" + cno + "&grade=" + grade);
}