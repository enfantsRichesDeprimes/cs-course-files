package org.example;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class AppTest {
    public static void main(String[] args) {
        // 初始化Spring容器
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(ThirdPartyConfig.class);

        // 获取被管理的Bean
        MyBean myBean = (MyBean) context.getBean("myBean");

        // 测试是否成功管理
        if (myBean != null) {
            System.out.println("Bean管理成功！");
        } else {
            System.out.println("Bean管理失败！");
        }

        // 关闭Spring容器
        context.close();
    }
}
