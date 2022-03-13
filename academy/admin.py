from django.contrib import admin

from .models import Instructor, Category, Course, Source, User, Comment


# Register your models here.
admin.site.site_header = "Academy platform"
admin.site.site_title = "Platform admin panel"
admin.site.index_title = ""


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'avatar', 'tutor_rating', )
    list_display_links = ('firstname', 'lastname',)
    list_filter = ('firstname', 'lastname', )
    search_fields = ('name', 'email', 'phone')

    fieldsets = (
        (None, {
            "fields": (
                'firstname', 'lastname', 'email', 'password', 'avatar', 'short_description', 
            ),
        }),
        ('Social media', {
            "classes": ('collapse',),
            "fields": (
                'instagram', 'facebook', 'linked_in', 'git_hub', 'portfolio',
            )
            }),
        
    )
    exclude = ('tutor_rating', 'registration_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image_preview', 'number_of_courses', 'is_active', )
    list_display_links = ('title',)
    # list_editable = ('is_active', )
    
    readonly_fields = ('get_image_preview',)
    
    @admin.action(description='Change to publish')
    def make_published(self, request, queryset):
        """change status of selected questions to True if status is False else False"""
        rows_updated = queryset.update(is_active=True)
        if rows_updated == 1:
            message_bit = ''
        else:
            message_bit = '{} course were'.format(rows_updated)
        self.message_user(request, '{} successfully published.'.format(message_bit))
    
    
    @admin.action(description='Change to unpublish')
    def make_unpublished(self, request, queryset):
        """change status of selected questions to False if status is True else True"""
        # queryset.update(status='p')
        
        rows_updated = queryset.update(is_active=False)
        if rows_updated == 1:
            message_bit = ''
        else:
            message_bit = '{} course were'.format(rows_updated)
        self.message_user(request, '{} successfully unpublished.'.format(message_bit))
    
    actions = ['make_published', 'make_unpublished']
    
class SourceInline(admin.StackedInline):
    model = Source
    extra = 1
    


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('categories', 'title', 'author', 'rate', 'level', 'price', 'is_active', )
    list_display_links = 'title',
    list_editable = ('is_active', )
    list_per_page = 10
    
    fieldsets = (
        (None, {
            "fields": (
                'categories', 'title', 'description', 'preview_image', 'level', 'price', 'author', 'is_active',
            )}
        ),
        ('Secondary information', {
            "classes": ('collapse',),
            "fields": (
                'overview', 'requirements', 'course_include',
            )}
        ),        
    )
    
    inlines = [SourceInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'email', 'phone', 'avatar', )
    list_display_links = ('username', 'firstname', 'lastname',)

    exclude = ('registration_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'text', 'date', 'rating')
    list_display_links = None
    
    actions = None
    
    def has_add_permission(self, request):
        return False
