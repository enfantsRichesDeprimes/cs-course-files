package org.example;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("org.example")
public class ThirdPartyConfig {
    @Bean
    public MyBean myBean() {
        return new MyBean();
    }
}