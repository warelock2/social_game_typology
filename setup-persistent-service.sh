#!/bin/bash -
sudo cp social_game_typology_quiz.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable social_game_typology_quiz.service
sudo systemctl start social_game_typology_quiz.service
