from sqlalchemy import true


{
    "git.autoRepositoryDetection": "subFolders",
    "breadcrumbs.enabled": true,

    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "off",
    "python.analysis.diagnosticMode": "openFilesOnly",
    "python.analysis.autoSearchPaths": true,
    "python.analysis.autoImportCompletions": true,
    "python.analysis.completeFunctionParens": true,
    "python.analysis.inlayHints.variableTypes": true,
    "python.analysis.inlayHints.functionReturnTypes": true,
    "python.analysis.importFormat": "absolute",
    "python.analysis.enablePytestSupport": true,
    "python.analysis.indexing": true,
    "python.analysis.packageIndexDepths": [
        {
            "name": "django",
            "depth": 3,
            "includeAllSymbols": true
        }
    ],
      
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "files.associations": {
        "**/*.html": "html",
        "**/templates/*/*.html": "django-html",
        "**/templates/*/*/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "django.snippets.exclude": [
        "cms",
        "wagtail"
    ],


    "[django-html]": {
        "editor.defaultFormatter": "batisteo.vscode-django",
        "breadcrumbs.showClasses": true,
        "editor.quickSuggestions": {
            "other": true,
            "comments": true,
            "strings": true
        }
    }
}