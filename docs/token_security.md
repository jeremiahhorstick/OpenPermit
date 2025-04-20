
# Secure GitHub Token Management

## Best Practices for Token Rotation

1. **Regular Rotation Schedule**
   - Rotate tokens every 30-90 days
   - Set calendar reminders for token expiration
   - Use automated rotation scripts when possible

2. **Security Measures**
   - Never commit tokens to git repository
   - Use environment variables when possible
   - Store tokens with restricted permissions (600)
   - Use minimal required scopes for tokens

3. **Backup Procedures**
   - Keep backup of previous token until new one is verified
   - Store backups in secure location
   - Clean up old backups regularly

4. **Monitoring**
   - Monitor token usage through GitHub audit logs
   - Watch for unauthorized access attempts
   - Review token permissions regularly

5. **Emergency Procedures**
   - Have plan for immediate token revocation
   - Maintain list of systems using token
   - Document recovery procedures
