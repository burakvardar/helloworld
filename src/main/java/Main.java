package com.example;

import org.glassfish.jersey.server.ResourceConfig;

public class Main {
    public static void main(String[] args) {
        ResourceConfig config = new ResourceConfig(HelloWorld.class);
        config.packages("org.glassfish.jersey.jackson");

        org.glassfish.jersey.server.Server server = org.glassfish.jersey.server.ServerBuilder
                .create().config(config).build();

        server.start();

        System.out.println("Jersey app started at http://localhost:8080/");
        System.out.println("Press Ctrl+C to stop the server.");
    }
}

