# This is a Feature file
Feature: 메인페이지
    @JIRA-ID
    Scenario: FaceSDK
        Given 기초설정 + 앱 진입하기
        When 신분증 촬영 대기하기
        Then 결과값 받아오기

