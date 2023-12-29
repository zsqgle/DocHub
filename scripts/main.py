"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 29/12/2023
@Description  :
"""
from scripts.logs.config import setup_logging
from scripts.readme_handler import update_readme

if __name__ == '__main__':
    setup_logging()
    update_readme()
