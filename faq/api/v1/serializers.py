from json.decoder import NegInf

from rest_framework import serializers

from ...models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "text"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ["pk", "text", "answers"]

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()

        answers = validated_data.get('answers')
        if answers:
            has_answers = {answer.pk: answer for answer in instance.answers.all()}
            for answer in answers:
                answer_id = answer.get('id')
                if answer_id and answer_id in has_answers.keys():
                    has_answer = has_answers[answer_id]
                    has_answer.text = answer.get('text', has_answer.text)
                    has_answer.save()
                else:
                    Answer.objects.create(question=instance, **answer)

        return instance

    def create(self, validated_data):
        answers = validated_data.pop('answers')

        question = Question.objects.create(**validated_data)
        for answer in answers:
            Answer.objects.create(question=question, **answer)

        return question
