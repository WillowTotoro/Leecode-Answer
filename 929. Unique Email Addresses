class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        actual_emails = []
        for i in range(len(emails)):
            local, domain = tuple(emails[i].split('@'))
            local = local.split('+')[0]
            local = local.replace('.', '')
            actual_email = local+'@'+domain
            actual_emails.append(actual_email)
        count = len(set(actual_emails))
        return count
            
                
            
            
