#!/usr/bin/env python3
"""Replace auth.login with admin.login in admin.py"""

with open('backend/app/routes/admin.py', 'r') as f:
    content = f.read()

content = content.replace("url_for('auth.login')", "url_for('admin.login')")

with open('backend/app/routes/admin.py', 'w') as f:
    f.write(content)

print('✓ All auth.login redirects replaced with admin.login in admin.py')
