from enum import IntEnum

class Permission(IntEnum):
    READ =1
    WRITE = 2
    EXECUTE= 4


class Role:
    permissions =0 
    def add_permission(self,perm):
        if not self.has_permission(perm):
            self.permissions+=perm
    def has_permission(self,perm):
        return self.permissions & perm == perm

a = Role()

a.add_permission(Permission.READ)
a.add_permission(Permission.WRITE)
print(a.has_permission(Permission.READ))
print(a.has_permission(Permission.WRITE))
print(a.has_permission(Permission.EXECUTE))

for i in Permission:
    print(i,type(i))
    