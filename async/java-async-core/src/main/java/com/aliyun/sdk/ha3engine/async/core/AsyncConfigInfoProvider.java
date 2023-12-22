package com.aliyun.sdk.ha3engine.async.core;

import com.aliyun.auth.credentials.Credential;
import com.aliyun.auth.credentials.ICredential;
import com.aliyun.auth.credentials.exception.CredentialException;
import com.aliyun.auth.credentials.provider.ICredentialProvider;

/**
 * @Author maguoxin
 * @Date 2023-12-21 10:00
 **/
public class AsyncConfigInfoProvider implements ICredentialProvider {

    private Credential credential;

    private String username;

    private String password;

    public AsyncConfigInfoProvider(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public static AsyncConfigInfoProvider create(String username, String password) {
        return new AsyncConfigInfoProvider(username, password);
    }

    @Override
    public ICredential getCredentials() throws CredentialException {
        return this.credential;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    @Override
    public void close() {
    }
}
